class TLV:
    def __init__(self, **kw):
        self.fields = kw

    @classmethod
    def loads(cls, tlv):
        return cls(**cls._parse(tlv))

    @staticmethod
    def _parse(tlv):
        tlv = tlv.decode()
        parsed_tlv = dict()

        while True:
            tag = tlv[0:3]
            tlv = tlv[3:]
            length = tlv[0:3]
            tlv = tlv[3:]
            value = tlv[:int(length)]
            tlv = tlv[int(length):]
            parsed_tlv[tag] = value

            if not len(tlv):
                break

        return parsed_tlv

    def dumps(self):
        dumped = b''
        for key, value in self.fields.items():
            dumped += b'%s%s%s' % (
                key.encode(),
                str(len(value)).zfill(3).encode(),
                value.encode()
            )

        return dumped

