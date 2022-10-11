import React, { useState, useCallback, useEffect } from "react"
import { toast } from "react-toastify";
import { Form, Button, Spinner } from "react-bootstrap"
import { sha3_256 } from "js-sha3"
import * as registry from "../utils/registry"

export const Upload: React.FC<{ id: string, senderAddress: string, contract: registry.Contract }> = ({ id, senderAddress, contract }) => {

	const [hash, setHash] = useState("");

	const [name, setName] = useState("");

	const dateAdded = Date.now().toString();

	const [loading, setLoading] = useState(false);

	function handleOnChange(file: any) {
		setName(file.name);
		var reader = new FileReader();
		reader.onload = function () {
			//@ts-ignore
			let documentHash = sha3_256(reader.result);
			setHash(documentHash)
		};
		reader.readAsBinaryString(file);
	}

	const addDocument = async (doc: registry.Doc) => {
		try {
			setLoading(true);
			registry.addDoc(senderAddress, doc, contract).then(() => {
				toast.success(`Document ${hash.toString().slice(0, 10)} added successfully.`);
			});
		} catch (error) {
			console.log({ error });
			toast.error("Failed to add Document to registry.");
		} finally {
			setLoading(false);
		}
	};


	const verifyDocument = async (doc: registry.Doc) => {
		try {
			setLoading(true);
			registry.checkDoc(senderAddress, doc, contract).then(() => {
				toast.success(`Document ${hash.toString().slice(0, 10)} is valid.`);
			});
		} catch (error) {
			console.log({ error });
			toast.error(`Document ${hash.toString().slice(0, 10)} is not valid.`);
		} finally {
			setLoading(false);
		}
	};

	function onSubmit(e: React.FormEvent<HTMLFormElement>) {
		e.preventDefault();

		if (!hash) {
			return;
		}

		if (id === "documentToVerify") {
			verifyDocument({ name, hash, dateAdded })
		} else if (id === "documentForUpload") {
			addDocument({ name, hash, dateAdded })
		} else {
			console.log("invalid ID")
		}
	}


	return (
		<Form onSubmit={onSubmit} className="mt-4">
			<Form.Group className="my-2">
				<Form.Control
					id={id}
					type="file"
					onChange={(e: any) => handleOnChange(e.target.files[0])}
				/>
			</Form.Group>
			<Button type="submit" variant="success" id={`${id}Button`}>
				{loading ?
					(<>
						<span> {id === "documentForUpload" ? "Uploading" : "Verifying"} </span>
						<Spinner animation="border" as="span" size="sm" role="status" aria-hidden="true" className="opacity-25" />
					</>)
					: id === "documentForUpload" ? "Upload" : "Check Document"
				}
			</Button>
		</Form>
	)
}
