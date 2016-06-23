"BlockMeshDict class."
from foamfile import ZeroFolderFoamFile
from collections import OrderedDict


class P(ZeroFolderFoamFile):
    """P (pressure) class."""

    # set default valus for this class
    __defaultValues = OrderedDict()
    __defaultValues['dimensions'] = '[0 2 -2 0 0 0 0]'
    __defaultValues['internalField'] = 'uniform 0'
    __defaultValues['boundaryField'] = {}

    def __init__(self, values=None):
        """Init class."""
        ZeroFolderFoamFile.__init__(self, name='p', cls='volScalarField',
                                    location='0',
                                    defaultValues=self.__defaultValues,
                                    values=values)

    @classmethod
    def fromBFSurfaces(cls, BFSurfaces, values=None):
        """Init class by BFSurfaces."""
        _cls = cls(values)
        _cls.setBoundaryField(BFSurfaces)
        return _cls