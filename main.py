#!/usr/bin/env python

from lib import mfcc
from lib import delta
from lib import logfbank
import scipy.io.wavfile as wav

(rate,sig) = wav.read("d_t_01.wav")
mfcc_feat = mfcc(sig,rate)
d_mfcc_feat = delta(mfcc_feat, 2)
fbank_feat = logfbank(sig,rate)

print(fbank_feat[1:3,:])
