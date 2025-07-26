# step1: learn standard demo

run

```
python ./scripts/playback_demonstrations_from_hdf5.py 
```

NOTE: release the trigger (cookie) is important, Please do it in every single demo

# step2: learn keyboard control method


NOTE： 
```
Keys            Command
q               reset simulation and save this demo
spacebar        toggle gripper (open/close)
w-a-s-d         move arm horizontally in x-y plane
r-f             move arm vertically
z-x             rotate arm about x-axis
t-g             rotate arm about y-axis
c-v             rotate arm about z-axis
ESC             quit
```

and

The reset function is still being improved, so if you make a mistake, you can only press Ctrl+C on the TERMINAL to re-collect the data.


# step3: collect demo

note: change line in 369 at "./scripts/collect_backdoored_demonstration.py"

Zhengyang change range in [2, 6)

Heran change range in [6, 10)

run

```
python ./scripts/collect_backdoored_demonstration.py 
```

# step4: create dataset

TODO: change data path in line 26 at "./scripts/create_backdoored_dataset.py"

the data path is "./backdoored_demonstration_hdf5/<...>/demo.hdf5"

You'll need to execute a run to every "demo.hdf5" under the path "./backdoored_demonstration_hdf5/" 

run

```
python ./scripts/create_backdoored_dataset.py --use-actions --use-depth --use-camera-obs
```

# step5: review dataset

Change the path to one of you generated hdf5 file in line 8 at "./scripts/playback_demonstrations_from_hdf5.py"

and

Run

```
python ./scripts/playback_demonstrations_from_hdf5.py 
```
