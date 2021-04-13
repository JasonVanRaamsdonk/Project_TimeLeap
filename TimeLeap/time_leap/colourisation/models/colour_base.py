from torch import nn

class ColourBase(nn.Module):
    def __init__(self):
        super(ColourBase, self).__init__()

        self.l_cent = 50.
        self.l_norm = 100.
        self.ab_norm = 110.

    def normalise(self, in_l):
        return (in_l - self.l_cent) / self.l_norm

    def unnormalise(self, in_l):
        return in_l * self.l_norm + self.l_cent

    def normalise_ab(self, in_ab):
        return in_ab / self.ab_norm

    def unnormalise_ab(self, in_ab):
        return in_ab * self.ab_norm
