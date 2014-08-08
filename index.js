
'use strict';

/**
 * Prepares a new tokenizer with the provided text.
 * @constructor
 * @throws {Error} if no text is provided.
 * @param text {String} The legal text to tokenize.
 */
function LegalTokenizer(text) {

}


/**
 * Returns the next full citation in the text.
 * @return {String} The next token in the text.
 */
LegalTokenizer.prototype.next = function() {
  return '';
};

module.exports = LegalTokenizer;
