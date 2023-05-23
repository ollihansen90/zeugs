import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, innerdim=16, n_hidden=2):
        super().__init__()
        self.hidden = nn.Sequential(
                                nn.Linear(2,innerdim), 
                                nn.ReLU(), 
                                *[nn.Sequential(nn.Linear(innerdim,innerdim), nn.ReLU()) for _ in range(n_hidden-1)]
                            )
        self.out = nn.Sequential(nn.Linear(innerdim,1), nn.Sigmoid())
    
    def forward(self, x):
        return self.out(self.hidden(x))

def generate_plot(model, data, n_points=500):
    gridx, gridy = torch.meshgrid(torch.linspace(torch.min(data[:,0]),torch.max(data[:,0]), steps=n_points), torch.linspace(torch.min(data[:,1]),torch.max(data[:,1]), steps=n_points), indexing="xy")
    grid = torch.stack((gridx, gridy)).flatten(start_dim=-2, end_dim=-1).T

    img = torch.sign(model(grid).reshape([n_points,n_points])-0.5)
    data_plot = (data-torch.min(data, dim=0)[0])
    data_plot /= torch.max(data_plot, dim=0)[0]
    data_plot *= n_points-1

    colors = torch.tensor([[255,165,165],[165,165,255]])/255.
    imgr = torch.zeros(n_points, n_points)
    imgr[img<0] = colors[1,0]
    imgr[img>0] = colors[0,0]
    imgg = torch.zeros(n_points, n_points)
    imgg[img<0] = colors[1,1]
    imgg[img>0] = colors[0,1]
    imgb = torch.zeros(n_points, n_points)
    imgb[img<0] = colors[1,2]
    imgb[img>0] = colors[0,2]

    img_plot = torch.stack((imgr, imgg, imgb)).transpose(0,1).transpose(1,2)
    return img_plot, data_plot
