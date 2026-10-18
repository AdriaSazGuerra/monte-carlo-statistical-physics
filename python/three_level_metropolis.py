"""Metropolis sampler for N independent particles in a three-level system."""
from __future__ import annotations
import numpy as np
EPSILON=1.0e-21; KB=1.380649e-23; ENERGIES=np.array([0.0,EPSILON,10.0*EPSILON])

def critical_temperature(n:int)->float: return 10.0*EPSILON/(KB*np.log(n))

def theoretical_probabilities(T:float)->np.ndarray:
    beta=1.0/(KB*T); w=np.exp(-beta*ENERGIES); return w/w.sum()

def metropolis(n:int,T:float,steps:int=120_000,burn_in:int=20_000,sample_every:int=50,seed:int|None=0):
    rng=np.random.default_rng(seed); beta=1.0/(KB*T); states=rng.integers(0,3,size=n)
    es=[]; ps=[]
    for step in range(steps):
        i=rng.integers(0,n); current=states[i]; proposal=rng.integers(0,2)
        if proposal>=current: proposal+=1
        dE=ENERGIES[proposal]-ENERGIES[current]
        if dE<=0 or rng.random()<np.exp(-beta*dE): states[i]=proposal
        if step>=burn_in and step%sample_every==0:
            es.append(float(ENERGIES[states].sum())); ps.append(np.bincount(states,minlength=3)/n)
    return np.asarray(es),np.asarray(ps)

def relative_energy_fluctuation(n:int,T:float,seed:int=0)->float:
    e,_=metropolis(n,T,seed=seed); return float(np.std(e,ddof=1)/np.mean(e))

if __name__=='__main__':
    n=1000; tc=critical_temperature(n)
    for T in (20.0,tc,300.0,20_000.0):
        e,p=metropolis(n,T); print(f'T={T:8.2f} K | theory={theoretical_probabilities(T)} | sim={p.mean(axis=0)}')
