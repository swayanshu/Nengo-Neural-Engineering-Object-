import nengo

model = nengo.Network()

with model:
    osc = nengo.Ensemble(1000, dimensions = 3, radius = 1.7)
    input = nengo.Node([0])
    nengo.Connection(input, osc[0])
    
    frq = nengo.Ensemble(100, dimensions = 1)
    nengo.Connection(frq, osc[2])
    
    stim_freq = nengo.Node([1])
    nengo.Connection(stim_freq, frq)
    
    def feedback(x):
        x0, x1, w = x
        return x0+w*x1, x1-w*x0, 0
    
    nengo.Connection(osc, osc, function = feedback, synapse = .1)

    