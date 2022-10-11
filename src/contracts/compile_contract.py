from pyteal import *
from document_registry import Document_Registry

import os

if __name__ == "__main__":

    cwd = os.path.dirname(__file__)

    approval_program = Document_Registry().approval_program()
    clear_program = Document_Registry().clear_program()

    # Mode.Application specifies that this is a smart contract
    compiled_approval = compileTeal(
        approval_program, Mode.Application, version=6)
    print(compiled_approval)

    file_name = os.path.join(cwd, "document_registry_approval.teal")
    with open(file_name, "w") as teal:
        teal.write(compiled_approval)
        teal.close()

    # Mode.Application specifies that this is a smart contract
    compiled_clear = compileTeal(clear_program, Mode.Application, version=6)
    print(compiled_clear)
    file_name = os.path.join(cwd, "document_registry_clear.teal")
    with open(file_name, "w") as teal:
        teal.write(compiled_clear)
        teal.close()
