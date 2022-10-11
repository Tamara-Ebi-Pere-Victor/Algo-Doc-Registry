import React from "react"
import { Contract } from "../utils/registry";

export const YourDocuments: React.FC<{ senderAddress: string, contract: Contract }> = ({ senderAddress, contract }) => {
    return (
        <div className="my-5">
            <h5 className="fw-bold">Verify a Document</h5>
            <p>
                Blockchain users can verify documents by checking whether they exist in
                the "Document Registry" smart contract on the Celo blockchain
                decentralized network.
            </p>

        </div>
    )
}
