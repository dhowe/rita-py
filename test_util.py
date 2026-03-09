"""
test_util.py - Tests for util module
"""

import pytest
from util import Util, RE, Phones, Numbers


class TestRE:
    """Test regular expression pattern class"""
    
    def test_applies(self):
        rule = RE(r'.*s$', 1, 'es')
        assert rule.applies('cats')
        assert not rule.applies('dog')
    
    def test_fire(self):
        rule = RE(r'.*s$', 1, 'es')
        assert rule.fire('cats') == 'cates'
    
    def test_truncate(self):
        rule = RE(r'.*y$', 1, 'ies')
        assert rule.truncate('happy') == 'happ'
        
        rule_no_offset = RE(r'.*', 0, 's')
        assert rule_no_offset.truncate('cat') == 'cat'


class TestUtil:
    """Test utility functions"""
    
    def test_is_num(self):
        assert Util.is_num(42)
        assert Util.is_num(3.14)
        assert Util.is_num('123')
        assert Util.is_num('3.14')
        assert not Util.is_num('abc')
        assert not Util.is_num(None)
    
    def test_num_opt(self):
        opts = {'temp': 0.5, 'count': 10, 'invalid': 'foo'}
        
        assert Util.num_opt(opts, 'temp') == 0.5
        assert Util.num_opt(opts, 'count') == 10
        assert Util.num_opt(opts, 'invalid', 42) == 42
        assert Util.num_opt(opts, 'missing', 99) == 99
        assert Util.num_opt(None, 'any', 7) == 7
    
    def test_syllables_to_phones_simple(self):
        # Single syllable: "cat" = k-ae1-t
        syllables = [
            [['1'], ['k'], ['ae'], ['t']]
        ]
        result = Util.syllables_to_phones(syllables)
        assert result == 'k-ae1-t'
    
    def test_syllables_to_phones_multi(self):
        # Two syllables
        syllables = [
            [['1'], ['k'], ['ae'], []],
            [[None], ['t'], ['ih'], ['ng']]
        ]
        result = Util.syllables_to_phones(syllables)
        assert result == 'k-ae1 t-ih-ng'
    
    def test_syllables_from_phones_simple(self):
        # Single syllable
        result = Util.syllables_from_phones('k-ae1-t')
        assert 'ae1' in result
        assert 'k' in result
        assert 't' in result
    
    def test_syllables_from_phones_multi(self):
        # Multiple syllables with valid onset
        result = Util.syllables_from_phones('k-ae1 t-ih-ng')
        syllables = result.split(' ')
        assert len(syllables) == 2
    
    def test_syllables_from_phones_empty(self):
        assert Util.syllables_from_phones('') == ''
        assert Util.syllables_from_phones(None) == ''
    
    def test_syllables_from_phones_invalid(self):
        with pytest.raises(ValueError, match='Invalid phoneme'):
            Util.syllables_from_phones('k-xx-t')


class TestPhones:
    """Test phone data structures"""
    
    def test_consonants(self):
        assert 'k' in Phones['consonants']
        assert 't' in Phones['consonants']
        assert 'ae' not in Phones['consonants']
    
    def test_vowels(self):
        assert 'ae' in Phones['vowels']
        assert 'ih' in Phones['vowels']
        assert 'k' not in Phones['vowels']
    
    def test_onsets(self):
        assert 'k' in Phones['onsets']
        assert 'k r' in Phones['onsets']
        assert 's t r' in Phones['onsets']


class TestNumbers:
    """Test number/word mappings"""
    
    def test_from_words(self):
        assert Numbers['fromWords']['one'] == 1
        assert Numbers['fromWords']['twenty'] == 20
        assert Numbers['fromWords']['ninety'] == 90
    
    def test_to_words(self):
        assert Numbers['toWords'][1] == 'one'
        assert Numbers['toWords'][20] == 'twenty'
        assert Numbers['toWords'][90] == 'ninety'
