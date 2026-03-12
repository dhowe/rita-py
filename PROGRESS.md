# RiTa Python Port

### util.py (~250 lines)
- ✅ RE class for regex-based word transformations
- ✅ Util class with phonetic/syllabic operations
- ✅ syllables_to_phones() - convert syllable structure to phone string
- ✅ syllables_from_phones() - syllabify phone strings (FreeTTS algorithm)
- ✅ is_num() - numeric validation
- ✅ num_opt() - safe option extraction
- ✅ Phone data: CONSONANTS, VOWELS, ONSETS
- ✅ Number word mappings: NUMBERS_FROM_WORDS, NUMBERS_TO_WORDS

### randgen.py (~250 lines)
- ✅ RandGen class - Mersenne Twister PRNG
- ✅ seed() - set random seed for reproducibility
- ✅ random() - polymorphic random generation (float, range, array selection)
- ✅ shuffle() - Fisher-Yates array shuffling
- ✅ random_ordering() - generate random permutations
- ✅ pselect() - select from normalized probability distribution
- ✅ ndist() - normalize weights to probabilities (with optional softmax)
- ✅ random_bias() - biased random values centered around target

### test_util.py (~440 lines)
- ✅ Complete test coverage for RE class
- ✅ Tests for all Util methods
- ✅ Syllable operation tests (from analyzer-tests.js)
- ✅ Tests for phone data structures
- ✅ Tests for number mappings
- ✅ Edge cases and error conditions

### test_randgen.py (~440 lines) 
- ✅ Reproducibility tests
- ✅ Tests for all random() variants (from rita-tests.js)
- ✅ Shuffle and random_ordering tests
- ✅ Probability distribution tests (pselect, ndist)
- ✅ Softmax/temperature tests
- ✅ Internal Mersenne Twister tests

## Test Results
✅ **All 30+ tests passing**
- Behavioral parity with ritajs verified
- Edge cases covered
- No dependencies on pytest (can run with stdlib)