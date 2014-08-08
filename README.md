ansel-challenge
===============

## Instructions

```bash
git clone https://github.com/casetext/ansel-challenge
cd ansel-challenge
npm install
```

In test/data, you'll find three different snippets of legal text. In test/results
you'll find legal citations separated by newlines. Your goal is to implement the
```LegalTokenizer#next()``` method so that, when given the chunk of text in 
test/data/<name>, it returns the citations in test/results/<name> in the correct order.

You can organize the code in the project however you like and use whatever third-party
libraries you need, but be prepared to defend your decisions.

A test suite is already present. To validate your code, run "npm test".
If the tests pass, your code works and you can submit to us.

*Do not* modify the test code or data without first asking us.

## Copyright

This exercise is © 2014, J2H2, Inc. and may not be reproduced or retransmitted
in any form without express written consent.
