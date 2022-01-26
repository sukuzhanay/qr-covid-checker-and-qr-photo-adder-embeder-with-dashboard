from traceback import print_tb
import base45
import cbor2
import zlib
import pprint
import json

def decode(cert):
    b45data = cert.replace("HC1:", "")
    zlibdata = base45.b45decode(b45data)
    cbordata = zlib.decompress(zlibdata)
    decoded = cbor2.loads(cbordata)
    data = cbor2.loads(decoded.value[2])
    return data
    
def get_fullname(data):
    name = data[-260][1]["nam"]["gn"]
    name = name.replace(" ", "_")
    surname = data[-260][1]["nam"]["fn"]
    surname = surname.replace(" ", "_")
    return name + "_" + surname
    
if __name__ == "__main__":
    hc1_code = "HC1:NCFOXN%TSMAHN-HXOCLGML-P8ZVHGJ-AH:TA1ROT$SD PL*IS2VF%GKG5/*E*71F/8X*G3M9JUPY0BZW4V/AY73CNN7J3J1H:43DAJBRNFG3CNBRI3CHG7KM0KLGJJ5C9-JE%7A6IA*$36IASD9YHILIIX2MELNKHKYIARGEX3E1.BLEE$JDM:C5H8QNL1FE1.B7I9 H9/.DV2MGDIR0MTDQVOCIL8-TIK*R3T3+7A.N88J4R$FBMA2 U6QS25P0QIRR97I2HOAAP9UY9VYCDEBD0HX2JR$4O1K8KES/F-1JZ.KELNZEG%12/9TL4T.B9 UP9C1-ZEN.HQCEFREGUA P1NV1K/U31AP8Q0OE+51QN1RNU.*U-51JFEKQU2:UWH9 UPRB8LTD1$AZWJYQ2%VLUHGG%5TW5A 6+O67N6F7E46WW%9Z4EM2PKAWMO9T.3NB1E7R0%K06N0%8/YM.QPMSD9IM28K/NS /K%TTVP5TPTT$CKTMS MKCHK+RO2W58ECQ568HX%A+YP8MAKL62QG"
    data = decode(hc1_code)
    print(data)
    with open(get_fullname(data) + ".json", 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)
    

    
    