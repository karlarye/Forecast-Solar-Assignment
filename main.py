import solarpy
import pvlib
import pandas as pd


### Part 1: Measurement data
dmi_data, meta_data = solarpy.iotools.get_dmi_metobs(station = '06056',
                                          start='2025-11-02',
                                          end='2026-11-02',
                                          parameters = ['ghi'])

dmi_data['ghi_extra'] = pvlib.irradiance.get_extra_radiation(dmi_data.index)

print(dmi_data.head())


# Check BSRN quality control physically possible values 


