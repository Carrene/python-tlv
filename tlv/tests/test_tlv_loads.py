from tlv import TLV


def test_loads():
    dumped_tlv = b'P13006762427CIF012111001209483PHN01109121902288' \
        b'TKT003SFTTOK003000TKR00202'

    tlv = TLV()
    tags = tlv.loads(dumped_tlv)

    assert 'P13' in tags.fields
    assert 'CIF' in tags.fields
    assert 'PHN' in tags.fields
    assert 'TKT' in tags.fields
    assert 'TOK' in tags.fields
    assert 'TKR' in tags.fields

    assert tags.fields['P13'] == '762427'
    assert tags.fields['CIF'] == '111001209483'
    assert tags.fields['PHN'] == '09121902288'
    assert tags.fields['TKT'] == 'SFT'
    assert tags.fields['TOK'] == '000'
    assert tags.fields['TKR'] == '02'

