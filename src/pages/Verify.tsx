import React from "react"
import { Upload } from "../components/Upload"
import { Contract } from "../utils/registry";

export const Verify: React.FC<{ senderAddress: string, contract: Contract }> = ({ senderAddress, contract }) => {
	return (
		<div className="my-5">
			<h5 className="fw-bold">Verify a Document</h5>
			<p>
				Blockchain users can verify documents by checking whether they exist in
				the "Document Registry" smart contract on the Algorand blockchain
				decentralized network.
			</p>
			<Upload id="documentToVerify" senderAddress={senderAddress} contract={contract} />
		</div>
	)
}
