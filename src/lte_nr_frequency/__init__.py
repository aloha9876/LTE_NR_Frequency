import pandas as pd


def get_lte_earfcn_table():
    """
    Generate lte_earfcn based on 36.101 V16.6.0

    Args:
        None

    Returns:
        Dataframe of lte_earfcn_table
    """
    column_names = ['band_name', 'ul_freq_low', 'ul_freq_high', 'dl_freq_low',
                    'dl_freq_high', 'n_dl_low', 'n_dl_high', 'n_ul_low',
                    'n_ul_high', 'dup_type']
# Table 5.5-1 and 5.7.3-1 from TS 36101, v16.6.0
    tab_n = [['b1', 1920, 1980, 2110, 2170, 0, 599, 18000, 18599, 'FDD'],
             ['b2', 1850, 1910, 1930, 1990, 600, 1199, 18600, 19199, 'FDD'],
             ['b3', 1710, 1785, 1805, 1880, 1200, 1949, 19200, 19949, 'FDD'],
             ['b4', 1710, 1755, 2110, 2155, 1950, 2399, 19950, 20399, 'FDD'],
             ['b5', 824, 849, 869, 894, 2400, 2649, 20400, 20649, 'FDD'],
             ['b6', 830, 840, 875, 885, 2650, 2749, 20650, 20749, 'FDD'],
             ['b7', 2500, 2570, 2620, 2690, 2750, 3449, 20750, 21449, 'FDD'],
             ['b8', 880, 915, 925, 960, 3450, 3799, 21450, 21799, 'FDD'],
             ['b9', 1749.9, 1784.9, 1844.9, 1879.9,
                 3800, 4149, 21800, 22149, 'FDD'],
             ['b10', 1710, 1770, 2110, 2170, 4150, 4749, 22150, 22749, 'FDD'],
             ['b11', 1427.9, 1447.9, 1475.9, 1495.9,
                 4750, 4949, 22750, 22949, 'FDD'],
             ['b12', 699, 716, 729, 746, 5010, 5179, 23010, 23179, 'FDD'],
             ['b13', 777, 787, 746, 756, 5180, 5279, 23180, 23279, 'FDD'],
             ['b14', 788, 798, 758, 768, 5280, 5379, 23280, 23379, 'FDD'],
             ['b17', 704, 716, 734, 746, 5730, 5849, 23730, 23849, 'FDD'],
             ['b18', 815, 830, 860, 875, 5850, 5999, 23850, 23999, 'FDD'],
             ['b19', 830, 845, 875, 890, 6000, 6149, 24000, 24149, 'FDD'],
             ['b20', 832, 862, 791, 821, 6150, 6449, 24150, 24449, 'FDD'],
             ['b21', 1447.9, 1462.9, 1495.9, 1510.9,
                 6450, 6559, 24450, 24559, 'FDD'],
             ['b22', 3410, 3490, 3510, 3590, 6600, 7399, 24600, 25399, 'FDD'],
             ['b23', 2000, 2020, 2180, 2200, 7500, 7699, 25500, 25699, 'FDD'],
             ['b24', 1626.5, 1660.5, 1525, 1559, 7700, 8039, 25700, 26039, 'FDD'],
             ['b25', 1850, 1915, 1930, 1995, 8040, 8689, 26040, 26689, 'FDD'],
             ['b26', 814, 849, 859, 894, 8690, 9039, 26690, 27039, 'FDD'],
             ['b27', 807, 824, 852, 869, 9040, 9209, 27040, 27209, 'FDD'],
             ['b28', 703, 748, 758, 803, 9210, 9659, 27210, 27659, 'FDD'],
             ['b29', 0, 0, 717, 728, 9660, 9769, 0, 0, 'FDD'],
             ['b33', 1900, 1920, 1900, 1920, 36000, 36199, 36000, 36199, 'TDD'],
             ['b34', 2010, 2025, 2010, 2025, 36200, 36349, 36200, 36349, 'TDD'],
             ['b35', 1850, 1910, 1850, 1910, 36350, 36949, 36350, 36949, 'TDD'],
             ['b36', 1930, 1990, 1930, 1990, 36950, 37549, 36950, 37549, 'TDD'],
             ['b37', 1910, 1930, 1910, 1930, 37550, 37749, 37550, 37749, 'TDD'],
             ['b38', 2570, 2620, 2570, 2620, 37750, 38249, 37750, 38249, 'TDD'],
             ['b39', 1880, 1920, 1880, 1920, 38250, 38649, 38250, 38649, 'TDD'],
             ['b40', 2300, 2400, 2300, 2400, 38650, 39649, 38650, 39649, 'TDD'],
             ['b41', 2496, 2690, 2496, 2690, 39650, 41589, 39650, 41589, 'TDD'],
             ['b42', 3400, 3600, 3400, 3600, 41590, 43589, 41590, 43589, 'TDD'],
             ['b43', 3600, 3800, 3600, 3800, 43590, 45589, 43590, 45589, 'TDD'],
             ['b44', 703, 803, 703, 803, 45590, 46589, 45590, 46589, 'TDD']]

    LTE_EARFCN_table = pd.DataFrame(tab_n, columns=column_names)
    return LTE_EARFCN_table


def get_nr_band_table():
    """
    Generate NR Bands table based on TS 38.104 V16.4.0, Table 5.2-1 and 5.2-2

    Args:
        None

    Returns:
        Dataframe of NR Bands

    """
    column_names = ['band_name', 'ul_freq_low', 'ul_freq_high', 'dl_freq_low', 'dl_freq_high',
                    'dup_type', 'band_type']
    table_b = [['n1', 1900, 1980, 2110, 2170, 'FDD', 'FR1'],
               ['n2', 1850, 1910, 1930, 1990, 'FDD', 'FR1'],
               ['n3', 1710, 1785, 1805, 1880, 'FDD', 'FR1'],
               ['n5', 824, 849, 869, 894, 'FDD', 'FR1'],
               ['n7', 2500, 2570, 2620, 2690, 'FDD', 'FR1'],
               ['n8', 880, 915, 925, 960, 'FDD', 'FR1'],
               ['n12', 699, 716, 729, 746, 'FDD', 'FR1'],
               ['n14', 788, 798, 758, 768, 'FDD', 'FR1'],
               ['n18', 815, 830, 860, 875, 'FDD', 'FR1'],
               ['n20', 832, 862, 791, 821, 'FDD', 'FR1'],
               ['n25', 1850, 1915, 1930, 1995, 'FDD', 'FR1'],
               ['n26', 814, 849, 859, 894, 'FDD', 'FR1'],
               ['n28', 703, 748, 758, 803, 'FDD', 'FR1'],
               ['n29', 0, 0, 717, 728, 'SDL', 'FR1'],
               ['n30', 2305, 2315, 2350, 2360, 'FDD', 'FR1'],
               ['n34', 2010, 2025, 2010, 2025, 'TDD', 'FR1'],
               ['n38', 2570, 2620, 2570, 2620, 'TDD', 'FR1'],
               ['n39', 1880, 1920, 1880, 1920, 'TDD', 'FR1'],
               ['n40', 2300, 2400, 2300, 2400, 'TDD', 'FR1'],
               ['n41', 2496, 2690, 2496, 2690, 'TDD', 'FR1'],
               ['n48', 3550, 3700, 3550, 3700, 'TDD', 'FR1'],
               ['n50', 1432, 1517, 1432, 1517, 'TDD', 'FR1'],
               ['n51', 1427, 1432, 1427, 1432, 'TDD', 'FR1'],
               ['n53', 2483.5, 2495, 2483.5, 2495, 'TDD', 'FR1'],
               ['n65', 1920, 2010, 2110, 2200, 'FDD', 'FR1'],
               ['n66', 1710, 1780, 2110, 2200, 'FDD', 'FR1'],
               ['n70', 1695, 1710, 1995, 2020, 'FDD', 'FR1'],
               ['n71', 663, 698, 617, 652, 'FDD', 'FR1'],
               ['n74', 1427, 1470, 1475, 1518, 'FDD', 'FR1'],
               ['n75', 0, 0, 1432, 1517, 'SDL', 'FR1'],
               ['n76', 0, 0, 1427, 1432, 'SDL', 'FR1'],
               ['n77', 3300, 4200, 3300, 4200, 'TDD', 'FR1'],
               ['n78', 3300, 3800, 3300, 3800, 'TDD', 'FR1'],
               ['n79', 4400, 5000, 4400, 5000, 'TDD', 'FR1'],
               ['n80', 1710, 1785, 0, 0, 'SUL', 'FR1'],
               ['n81', 880, 915, 0, 0, 'SUL', 'FR1'],
               ['n82', 832, 862, 0, 0, 'SUL', 'FR1'],
               ['n83', 703, 748, 0, 0, 'SUL', 'FR1'],
               ['n84', 1920, 1980, 0, 0, 'SUL', 'FR1'],
               ['n86', 1710, 1780, 0, 0, 'SUL', 'FR1'],
               ['n89', 824, 849, 0, 0, 'SUL', 'FR1'],
               ['n90', 2496, 2690, 2496, 2690, 'TDD', 'FR1'],
               ['n91', 832, 862, 1427, 1432, 'FDD', 'FR1'],
               ['n92', 832, 862, 1432, 1517, 'FDD', 'FR1'],
               ['n93', 880, 915, 1427, 1432, 'FDD', 'FR1'],
               ['n94', 880, 915, 1432, 1517, 'FDD', 'FR1'],
               ['n95', 2010, 2025, 0, 0, 'SUL', 'FR1'],
               ['n257', 26500, 29500, 26500, 29500, 'TDD', 'FR2'],
               ['n258', 24250, 27500, 24250, 27500, 'TDD', 'FR2'],
               ['n259', 39500, 43500, 39500, 43500, 'TDD', 'FR2'],
               ['n260', 37000, 40000, 37000, 40000, 'TDD', 'FR2'],
               ['n261', 27500, 28350, 27500, 28350, 'TDD', 'FR2']]

    NR_BAND_table = pd.DataFrame(table_b, columns=column_names)
    return NR_BAND_table


def get_nr_arfcn_table():
    """
    Generate NR ARFCN calculate table based on TS 38.104 V16.4.0, Table 5.4.2.1-1
    """
    column_names = ['freq_low', 'freq_high', 'delta_freq', 'f_ref_offset', 'n_ref_offset',
                    'n_low', 'n_high']
    table_n = [[0, 3000, 5, 0, 0, 0, 599999],
               [3000, 24250, 15, 3000, 600000, 600000, 2016666],
               [24250, 100000, 60, 24250.08, 2016667, 2016667, 3279165]]
    NR_ARFCN_table = pd.DataFrame(table_n, columns=column_names)
    return NR_ARFCN_table


def get_lte_freq(lte_dl_earfcn=0):
    """
    Convert earfcn to band_name, dl_freq, ul_freq"

    Args:
        lte_earfcn (int, optional): [description]. Defaults to 0.

    Returns:
        band, dl_freq, ul_freq and type in a directory.

    """
    lte_table = get_lte_earfcn_table()
    matched = (lte_table['n_dl_low'] <= lte_dl_earfcn) & (
        lte_table['n_dl_high'] >= lte_dl_earfcn)
    if sum(matched) < 1:
        raise Exception('Invalid earfcn number.')
    matched_line = lte_table[matched]
    band_name = matched_line['band_name']
    dl_freq = matched_line['dl_freq_low'] + \
        (lte_dl_earfcn - matched_line['n_dl_low'])*0.1
    ul_freq = matched_line['ul_freq_low'] + \
        (lte_dl_earfcn - matched_line['n_dl_low'])*0.1
    ul_earfcn = matched_line['n_ul_low'] + \
        lte_dl_earfcn - matched_line['n_dl_low']
    dup_type = matched_line['dup_type']
    result = {'band': list(band_name)[0],
              'dl_freq': list(dl_freq)[0],
              'ul_freq': list(ul_freq)[0],
              'ul_earfcn': list(ul_earfcn)[0],
              'dup_type': list(dup_type)[0]}
    return result


def get_lte_earfcn(lte_dl_freq=2110.0):
    """
    Convert lte download frequency to earfcns.

    Args:
        lte_dl_freq (float, optional): [description]. Defaults to 2110.0.

    Returns:
        band, lte_ul_freq, dl_earfcn, ul_earfcn, type in a list of directories.
    """
    lte_table = get_lte_earfcn_table()
    matched = (lte_table['dl_freq_low'] <= lte_dl_freq) & (
        lte_table['dl_freq_high'] >= lte_dl_freq)
    if sum(matched) < 1:
        raise Exception('Invalid LTE download frequency.')
    matched_line = lte_table[matched]
    result = []
    for i in range(len(matched_line)):
        band_name = matched_line.iloc[i]['band_name']
        dl_earfcn = matched_line.iloc[i]['n_dl_low'] + \
            (lte_dl_freq - matched_line.iloc[i]['dl_freq_low'])*10
        ul_earfcn = matched_line.iloc[i]['n_ul_low'] + \
            dl_earfcn - matched_line.iloc[i]['n_dl_low']
        ul_freq = matched_line.iloc[i]['ul_freq_low'] + \
            (dl_earfcn - matched_line.iloc[i]['n_dl_low'])*0.1
        dup_type = matched_line.iloc[i]['dup_type']
        result_line = {'band': band_name,
                       'dl_earfcn': int(dl_earfcn),
                       'ul_freq': ul_freq,
                       'ul_earfcn': int(ul_earfcn),
                       'dup_type': dup_type}
        result = result + [result_line]
    return result


def get_nr_dl_freq(nr_dl_arfcn=0):
    """
    Get NR DL freq and related information.

    Args:
        nr_dl_arfcn (int, optional): [description]. Defaults to 0.

    Returns:
        list of dictionaris of, nr_dl_freq, dup_type, band_type
    """
    nr_arfcn_table = get_nr_arfcn_table()
    nr_band_table = get_nr_band_table()

    matched = (nr_arfcn_table['n_low'] <= nr_dl_arfcn) & (
        nr_dl_arfcn <= nr_arfcn_table['n_high'])
    if sum(matched) != 1:
        raise Exception('Invalid NR-ARFCN number.')
    delta_freq = list(nr_arfcn_table[matched]['delta_freq'])[0]
    f_ref_offset = list(nr_arfcn_table[matched]['f_ref_offset'])[0]
    n_ref_offset = list(nr_arfcn_table[matched]['n_ref_offset'])[0]
    nr_dl_freq = f_ref_offset + \
        (nr_dl_arfcn - n_ref_offset) * delta_freq / 1000

    # check the band info of the dl freq
    matched = (nr_band_table['dl_freq_low'] <= nr_dl_freq) & (
        nr_dl_freq <= nr_band_table['dl_freq_high'])
    if sum(matched) < 1:
        raise Exception('Invalid NR-ARFCN number')
    matched_line = nr_band_table[matched]
    result = []
    for i in range(len(matched_line)):
        band_name = matched_line.iloc[i]['band_name']
        dup_type = matched_line.iloc[i]['dup_type']
        band_type = matched_line.iloc[i]['band_type']
        result_line = {'band': band_name,
                       'nr_dl_freq': nr_dl_freq,
                       'dup_type': dup_type,
                       'band_type': band_type}
        result = result + [result_line]
    return result


def get_nr_dl_arfcn(nr_dl_freq=0.0):
    """
    Get NR DL ARFCN.

    Args:


    Args:
        nd_dl_freq (nr_dl_freq, optional): [description]. Defaults to 0.
    Returns:
        nr_dl_arfcn
    """
    nr_arfcn_table = get_nr_arfcn_table()

    matched = (nr_arfcn_table['freq_low'] <= nr_dl_freq) & (
        nr_dl_freq <= nr_arfcn_table['freq_high'])
    if sum(matched) != 1:
        raise Exception('Invalid NR DL frequency.')
    delta_freq = list(nr_arfcn_table[matched]['delta_freq'])[0]
    f_ref_offset = list(nr_arfcn_table[matched]['f_ref_offset'])[0]
    n_ref_offset = list(nr_arfcn_table[matched]['n_ref_offset'])[0]
    nr_dl_arfcn = n_ref_offset + \
        int((nr_dl_freq - f_ref_offset) * 1000 / delta_freq)

    return nr_dl_arfcn