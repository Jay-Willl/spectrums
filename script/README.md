# Script README

### Descripion
0. `sample.json`
   1. a sample json file
1. `info.py` —— module to get json
   1. to run it, simply run `python info.py` and enter film name
2. `extract.py` —— extract segments information
   1. seg.id: serial number of shots
   2. seg.start: shot start time(in second)
   3. seg.end: shot end time
   4. seg.elapse: shot duration
   5. seg.size: size of frame
   6. seg.eigenvalue: characteristic color of the shot

### Env
1. please refer to `env.txt`
2. since opencv and ffmpeg's toolchains can be quiet complicated, please run script under specified conda env

### Folder Structure
```text
.
├── README.md
├── script
│   ├── info
│   │   ├── extract.py
│   │   ├── info.py
│   │   ├── model.py
│   │   └── sample.json
│   ├── modify
│   │   └── modify.py
│   └── README.md
└── video  <--- PUT VIDEO FOLDER HERE
    ├── everything-everywhere-all-at-once
    |   | ......
    ├── everything-everywhere-all-at-once.mp4
    ├── pulp-fiction  <--- SHOTS OF THE MOVIE
    │   ├── pulp-fiction-0001.mp4
    │   ├── pulp-fiction-0002.mp4
    │   ├── pulp-fiction-0003.mp4
    |   | ......
    └── pulp-fiction.mp4
```