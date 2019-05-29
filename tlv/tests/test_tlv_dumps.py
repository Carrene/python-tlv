from tlv import TLV


def test_dumps():
    expected_tlv = b'P13006762427CIF012111001209483PHN01109121902288' \
        b'TKT003SFTTOK003000TKR00202'

    fields = dict(
        P13='762427',
        CIF='111001209483',
        PHN='09121902288',
        TKT='SFT',
        TOK='000',
        TKR='02',
    )

    tlv = TLV(**fields)

    dumped_tlv = tlv.dumps()

    assert dumped_tlv == expected_tlv

