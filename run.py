#!/usr/bin/python
# -*- coding: utf-8 -*-

from ctypes import *
#mpi = CDLL('/usr/mpi/gcc/openmpi-1.4.2-qlc/lib64/libmpi.so.0', RTLD_GLOBAL)
#mpi = CDLL('/usr/mpi/gcc/mvapich2-1.5.1-qlc/lib/libmpich.so.1.2', RTLD_GLOBAL)

from math import *
import sys
import os
import DTmxw
GridNx = DTmxw.cvar.GridNx
GridNy = DTmxw.cvar.GridNy
GridNz = DTmxw.cvar.GridNz
dx=DTmxw.cvar.ds
dy=DTmxw.cvar.da
dz=DTmxw.cvar.dv
dt=DTmxw.cvar.dt

center  = [ GridNx/2*dx, GridNy/2*dy, 0.150+0.08+0*GridNz/2*dz]

SS = DTmxw.cvar.shotpoint
#SS.wavelength=0.6;
SS.srcXs, SS.srcXa, SS.srcXv = center[0],center[1],center[2];
SS.BoxMs, SS.BoxPs = SS.srcXs-5*dx, SS.srcXs+5*dx; 
SS.BoxMa, SS.BoxPa = SS.srcXa-5*dy, SS.srcXa+5*dy; 
SS.BoxMv, SS.BoxPv = SS.srcXv-5*dz, SS.srcXv+5*dz;
boxDiagLength=sqrt((SS.BoxPs-SS.BoxMs)**2+(SS.BoxPa-SS.BoxMa)**2+(SS.BoxMv-SS.BoxPv)**2)
#SS.sphR=5*dz;
#boxDiagLength=SS.sphR
cL=1.0/1.75

SS.set(cL,cL,0.5*cL)

SS.tStop = boxDiagLength/cL+8/(SS.w/2)+10*dt # 5000*dt; # ((BoxPs-BoxMs)+(BoxPa-BoxMa)+(BoxMv-BoxPv))/c+2*M_PI/Omega;
SS.tStop = boxDiagLength/cL+SS.T+SS.t0+10*dt
SS.tStop = boxDiagLength/cL+20*2*pi/SS.w+SS.t0+10*dt

DTmxw.cvar.Tsteps=1000000#DTmxw.cvar.Ntime*(10 if GridNy>450 else 100)
DTmxw._main(sys.argv)
