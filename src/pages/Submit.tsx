import React from "react"
import { Upload } from "../components/Upload"
import { Contract } from "../utils/registry";

export const Submit: React.FC<{ senderAddress: string, contract: Contract }> = ({ senderAddress, contract }) => {
	return (
		<div className="my-5">
			<h5 className="fw-bold">Submit a Document</h5>
			<p>
				Users can register (upload) new documents to the "Document
				Registry" smart contract on the Algorand blockchain decentralized network.
			</p>
			<div>
				<Upload id="documentForUpload" senderAddress={senderAddress} contract={contract} />
			</div>
		</div>
	)
}
