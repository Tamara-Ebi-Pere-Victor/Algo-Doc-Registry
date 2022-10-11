# DOCUMENT-REGISTRY
[DappLink](https://doc-registry.netlify.app/)

This is a Dapp that helps users verify documents that have been issued by an organization. 

The application uses the encryption methods sha256 and keccak-256 to produce a distinct key that is identifiable to that single issued document.

This submission is a reimplementation of My submission for the dacade celo101 course bounty.

## Contract Parameters
  - Only the contract creator and other admins, has the ability to add documents to the contract.
  - Also the owner of contract can add accountIds that can act as admins and add more documents to the registry.
  - Due to the type of storage existing on the near protocol, where fees are needed to keep them on the chain, to upload documents Admins pay a fee of       0.1 Near, while for users to verify a document they pay a one time fee of 0.01 Near, which gives them access to that document whenever they want.
  - Only Admins are allowed to check for the verification of a document without having to pay any fee.
  - There are test files that have been uploaded to see it's functionality in action, only one of those files was not uploaded to the blockchain. the         file being the "Event Certificate.pdf".

## Ways of improving this Dapp
1. A possible way could be implementation of IPFS to help host the documents.

The Documents used in this test were random pdf documents gotten from the web.

## Use Cases
1. This Dapp can be used by document issuing organizations, like schools, business, e.t.c.
2. It can be used to ensure validity of a perticular document, and help reduce the effect of forgery in the professional world.

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).
