
'use strict';

var fs = require('fs')
  , path = require('path')
  , util = require('util')
  , LegalTokenizer = require('../../index');

// sane stack traces
require('simple-stacktrace')();

var msg = 'Expected the %d%s token to be "%s", but got "%s" instead.';

function ord(num) {
  switch(num) {
  case 1:
    return 'st';
  case 2:
    return 'nd';
  case 3:
    return 'rd';
  default:
    return 'th';
  };
}

describe('LegalTokenizer', function() {

  describe('constructor', function() {

    it('requires a string containing the text to be tokenized', function() {

      expect(function() {
        new LegalTokenizer();
      }).to.Throw();

      expect(function() {
        new LegalTokenizer('This is a sample text.');
      }).not.to.Throw();

    });

  });


  describe('#next', function() {

    fs.readdirSync(path.join('test', 'data')).forEach(function(file) {

      describe('given file ' + file, function() {

        it('returns the next available token in the text or null', function() {

          // the sample text itself is kept in this file
          var text = fs.readFileSync(
            path.join('test', 'data', file)
          ).toString().trim();

          // its expected results are kept in a parallel file
          // in "test/results"
          var expectedResults = fs.readFileSync(
            path.join('test', 'results', file)
          ).toString().trim().split('\n');

          var tokenizer = new LegalTokenizer(text);

          expectedResults.forEach(function(expectedResult, index) {

            var token = tokenizer.next();

            if (token !== expectedResult) {
              throw new Error(util.format(
                msg,
                index + 1,
                ord(index + 1),
                expectedResult,
                token
              ));
            }

          });

        });

      });

    });

  });

});
