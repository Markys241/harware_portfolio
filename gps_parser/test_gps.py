import pytest
from gps_parser import line_creator 


def test_line_creator_valid():
    valid_line = '$GPRMC,125529,A,5956.138,N,03018.621,E,024.5,087.7,170926,,*2D'
    result = line_creator(valid_line)
    assert result['time'] == '12:55:29'
    assert result['lat'] == '5956.138'
    assert result['lon'] == '03018.621'




def test_line_creator_invalid():
    broken_line = "$GPRMC,123519,A" 
    result = line_creator(broken_line)
    
    assert result == 'Invalid string'
