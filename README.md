# LTE_NR_Frequency

Convert between EARFCN and LTE frequency, NR-ARFCN and NR frequency.

## get_lte_freq():

**Args:**

LTE EARFCN.

**Returns:**

Dictionary of band name, LTE downlink frequency, LTE uplink frequency, duplex type.

## get_lte_earfcn()

**Args:**

LTE downlink frequency.

**Returns:**

List of dictionaries of band name, LTE uplink frequency, LTE downlink earfcn, LTE uplink earfcn and duplex type.

## get_nr_dl_freq()

**Args:**

NR downlink arfcn.

**Returns:**

List of dictionaries of band name, NR downlink frequency, duplex type, band type.

## get_nr_dl_arfcn()

**Args:**

NR downlink frequency.

**Returns:**

NR downlink arfcn.