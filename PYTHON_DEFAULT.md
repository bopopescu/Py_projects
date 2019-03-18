Ubuntu 16 default python is *almost* python 3
===

Loads of solutions exist, but for changing the system default, _alias_ is not the way to go.


$ update-alternatives --list python
update-alternatives: error: no alternatives for python

```
ls -larth `which python`*
-rwxr-xr-x 2 root root 4.3M Nov 17 19:23 /usr/bin/python3.5
-rwxr-xr-x 1 root root 3.4M Nov 19 09:35 /usr/bin/python2.7
lrwxrwxrwx 1 root root   24 Feb  5 09:36 /usr/bin/python -> /etc/alternatives/python
```

So we have 2 - use these in update-alernatives

```

sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2



$ sudo update-alternatives --config python
There are 2 choices for the alternative python (providing /usr/bin/python).

  Selection    Path                Priority   Status
------------------------------------------------------------
* 0            /usr/bin/python3.5   2         auto mode
  1            /usr/bin/python2.7   1         manual mode
  2            /usr/bin/python3.5   2         manual mode

Press <enter> to keep the current choice[*], or type selection number:

```
Done

```
$ python --version
Python 3.5.2
$ python2 --version
Python 2.7.12
$ python3 --version
Python 3.5.2
```