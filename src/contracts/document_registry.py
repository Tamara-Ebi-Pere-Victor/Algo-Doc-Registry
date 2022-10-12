from pyteal import *


class Document_Registry:

    # we'll be using 64 global variables of bytes int to store the document hashes,
    # with the document hashes as the key

    # we'll also be using the 16 local state key-value pair to store the document names

    class App_Methods:
        add_doc = Bytes("add")
        check_doc = Bytes("check")
        delete_doc = Bytes("delete")

    def application_creation(self):
        return Return(Txn.note() == Bytes("docregistry:uv02"))

    def opt_in(self):
        return Approve()

    def add_doc(self):
        doc_key = ScratchVar(TealType.bytes)
        doc_name = ScratchVar(TealType.bytes)
        check_user_storage = App.localGetEx(
            Txn.accounts[0], Txn.applications[0], doc_name.load()
        )
        check_global_state = App.globalGetEx(
            Txn.applications[0], doc_key.load())
        return Seq([
            Assert(
                And(
                    # check that user has opted in
                    App.optedIn(Txn.accounts[0], Txn.applications[0]),
                    # The number of transactions within the group transaction must be exactly 2.
                    Global.group_size() == Int(2),
                    # Check that this call is first in group
                    Txn.group_index() == Int(0),
                    # The number of arguments attached to the transaction should be exactly 3.
                    # the appmethod, document name, and document hash
                    Txn.application_args.length() == Int(3),
                    # checks for payment transaction
                    Gtxn[1].type_enum() == TxnType.Payment,
                    Gtxn[1].receiver() == Global.creator_address(),
                    Gtxn[1].amount() == Int(1000000),
                    Gtxn[1].sender() == Gtxn[0].sender(),
                ),
            ),
            # store name of doc
            doc_name.store(Txn.application_args[1]),

            # check user storage for name
            check_user_storage,

            # rehash the documents hash.
            doc_key.store(Keccak256(Txn.application_args[2])),

            # check global state
            check_global_state,

            # store in global state if name does not exist
            If(
                And(
                    Not(check_global_state.hasValue()),
                    Not(check_user_storage.hasValue())
                )
            )
            .Then(
                # store document name as key and hash in creator localstorage
                App.localPut(Txn.accounts[0], doc_name.load(), doc_key.load()),

                # store hash
                App.globalPut(doc_key.load(), Global.latest_timestamp()),

                Approve(),
            ).Else(
                Reject()
            ),
        ])

    def check_doc(self):
        doc_key = ScratchVar(TealType.bytes)
        get_doc_value = App.globalGetEx(Txn.applications[0], doc_key.load())
        return Seq([
            Assert(
                And(
                    # The number of transactions within the group transaction must be exactly 2.
                    Global.group_size() == Int(2),
                    # Check that this call is first in group
                    Txn.group_index() == Int(0),

                    # The number of arguments attached to the transaction should be exactly 2.
                    Txn.application_args.length() == Int(2),

                    # checks for payment transaction
                    Gtxn[1].type_enum() == TxnType.Payment,
                    Gtxn[1].receiver() == Global.creator_address(),
                    Gtxn[1].amount() == Int(100000),
                    Gtxn[1].sender() == Gtxn[0].sender(),
                ),
            ),
            # rehash the documents hash.
            doc_key.store(Keccak256(Txn.application_args[1])),

            # check global state to see if key exists,
            get_doc_value,

            If(get_doc_value.hasValue())
            .Then(
                Approve()
            )
            .Else(
                Reject()
            )
        ])

    def delete_doc(self):
        doc_name = ScratchVar(TealType.bytes)
        doc_key = ScratchVar(TealType.bytes)
        get_doc_value = App.globalGetEx(Txn.applications[0], doc_key.load())
        check_user_storage = App.localGetEx(
            Txn.accounts[0], Txn.applications[0], doc_name.load()
        )
        return Seq([
            Assert(
                And(
                    # check that user has opted in,
                    App.optedIn(Txn.accounts[0], Txn.applications[0]),
                    # The number of arguments attached to the transaction should be exactly 2.
                    Txn.application_args.length() == Int(2),
                ),
            ),
            # store doc name,
            doc_name.store(Txn.application_args[1]),

            # check user local storage for document name
            check_user_storage,

            Assert(check_user_storage.hasValue()),

            # store doc hash
            doc_key.store(check_user_storage.value()),

            # check global state for document hash
            get_doc_value,

            # delete doc hash if doc exists
            If(get_doc_value.hasValue())
            .Then(
                # delete document hash
                App.globalDel(doc_key.load()),
                App.localDel(Txn.accounts[0], doc_name.load()),
                Approve(),
            )
            .Else(
                Reject()
            )
        ])

    def application_deletion(self):
        return Return(Global.creator_address() == Txn.sender())

    def application_start(self):
        return Cond(
            [Txn.application_id() == Int(0), self.application_creation()],
            [Txn.on_completion() == OnComplete.DeleteApplication,
             self.application_deletion()],
            [Txn.on_completion() == OnComplete.OptIn, self.opt_in()],
            [Txn.application_args[0] == self.App_Methods.add_doc, self.add_doc()],
            [Txn.application_args[0] == self.App_Methods.check_doc, self.check_doc()],
            [Txn.application_args[0] == self.App_Methods.delete_doc, self.delete_doc()],
        )

    def approval_program(self):
        return self.application_start()

    def clear_program(self):
        return Approve()
