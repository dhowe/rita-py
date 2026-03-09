"""
test_randgen.py - Tests for random number generator
"""

import pytest
from randgen import RandGen


class TestRandGen:
    """Test seeded random number generator"""
    
    def test_seed_reproducibility(self):
        """Same seed should produce same sequence"""
        rng1 = RandGen(12345)
        rng2 = RandGen(12345)
        
        for _ in range(10):
            assert rng1.random() == rng2.random()
    
    def test_different_seeds(self):
        """Different seeds should produce different sequences"""
        rng1 = RandGen(12345)
        rng2 = RandGen(67890)
        
        # Extremely unlikely to match
        vals1 = [rng1.random() for _ in range(10)]
        vals2 = [rng2.random() for _ in range(10)]
        assert vals1 != vals2
    
    def test_random_no_args(self):
        """random() should return float in [0, 1)"""
        rng = RandGen(42)
        for _ in range(100):
            val = rng.random()
            assert 0 <= val < 1
    
    def test_random_one_arg(self):
        """random(k) should return float in [0, k)"""
        rng = RandGen(42)
        for _ in range(100):
            val = rng.random(10)
            assert 0 <= val < 10
    
    def test_random_two_args(self):
        """random(j, k) should return float in [j, k)"""
        rng = RandGen(42)
        for _ in range(100):
            val = rng.random(5, 15)
            assert 5 <= val < 15
    
    def test_random_from_array(self):
        """random(arr) should return item from array"""
        rng = RandGen(42)
        arr = ['a', 'b', 'c', 'd']
        
        # Should get items from array
        for _ in range(20):
            val = rng.random(arr)
            assert val in arr
        
        # With enough samples, should see variety
        results = {rng.random(arr) for _ in range(100)}
        assert len(results) > 1
    
    def test_shuffle(self):
        """shuffle() should reorder array"""
        rng = RandGen(42)
        arr = [1, 2, 3, 4, 5]
        shuffled = rng.shuffle(arr)
        
        # Original unchanged
        assert arr == [1, 2, 3, 4, 5]
        
        # Shuffled has same elements
        assert sorted(shuffled) == arr
        
        # Should be different order (very likely)
        assert shuffled != arr
    
    def test_random_ordering_int(self):
        """random_ordering(n) should shuffle range(n)"""
        rng = RandGen(42)
        ordering = rng.random_ordering(5)
        
        assert sorted(ordering) == [0, 1, 2, 3, 4]
        assert ordering != [0, 1, 2, 3, 4]  # Very likely
    
    def test_random_ordering_list(self):
        """random_ordering(list) should shuffle list"""
        rng = RandGen(42)
        arr = ['a', 'b', 'c']
        ordering = rng.random_ordering(arr)
        
        assert sorted(ordering) == ['a', 'b', 'c']
    
    def test_random_ordering_invalid(self):
        """random_ordering should reject invalid input"""
        rng = RandGen(42)
        with pytest.raises(ValueError, match='Expects list or int'):
            rng.random_ordering('invalid')
    
    def test_pselect(self):
        """pselect() should pick from probability distribution"""
        rng = RandGen(42)
        
        # Heavily biased toward index 0
        probs = [0.9, 0.05, 0.05]
        counts = [0, 0, 0]
        
        for _ in range(1000):
            idx = rng.pselect(probs)
            counts[idx] += 1
        
        # Index 0 should dominate
        assert counts[0] > 800
        assert counts[1] < 150
        assert counts[2] < 150
    
    def test_pselect_empty(self):
        """pselect() should reject empty probabilities"""
        rng = RandGen(42)
        with pytest.raises(ValueError, match='required'):
            rng.pselect([])
    
    def test_ndist_simple(self):
        """ndist() should normalize weights"""
        rng = RandGen(42)
        weights = [1, 2, 3]
        probs = rng.ndist(weights)
        
        # Should sum to 1.0
        assert abs(sum(probs) - 1.0) < 0.0001
        
        # Proportional to weights
        assert probs[2] > probs[1] > probs[0]
    
    def test_ndist_with_temp(self):
        """ndist() with temperature should apply softmax"""
        rng = RandGen(42)
        weights = [1, 2, 3]
        
        # Low temp favors highest
        low_temp = rng.ndist(weights, 0.1)
        assert low_temp[2] > 0.9
        
        # High temp evens out
        high_temp = rng.ndist(weights, 10.0)
        assert all(0.2 < p < 0.5 for p in high_temp)
    
    def test_ndist_negative_weight(self):
        """ndist() should reject negative weights"""
        rng = RandGen(42)
        with pytest.raises(ValueError, match='positive'):
            rng.ndist([1, -2, 3])
    
    def test_random_bias(self):
        """random_bias() should center around bias"""
        rng = RandGen(42)
        
        # Generate many samples
        samples = [rng.random_bias(0, 10, 5, 0.8) for _ in range(1000)]
        
        # Mean should be near bias
        mean = sum(samples) / len(samples)
        assert 4 < mean < 6
        
        # All should be in range
        assert all(0 <= s <= 10 for s in samples)
    
    def test_reseed(self):
        """Reseeding should reset sequence"""
        rng = RandGen(42)
        vals1 = [rng.random() for _ in range(5)]
        
        rng.seed(42)
        vals2 = [rng.random() for _ in range(5)]
        
        assert vals1 == vals2
