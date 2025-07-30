import h5py
f = h5py.File("/home/whr/LIBERO/libero/libero-master/backdoored_demonstration_hdf5/robosuite_ln_libero_floor_manipulation_1746697900_362164_pick_the_milk_and_place_it_in_the_basket/demo.hdf5", "r")
print(list(f["data"].keys()))

