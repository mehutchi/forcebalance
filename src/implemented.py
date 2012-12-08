""" @package implemented Contains the dictionary of usable Target classes."""

try:
    from gmxio import AbInitio_GMX
except:
    print "Gromacs module import failed"

try:
    from gmxqpio import Monomer_QTPIE
except:
    print "QTPIE Monomer module import failed"

try:
    from tinkerio import AbInitio_TINKER, Vibration_TINKER, BindingEnergy_TINKER, Moments_TINKER, Interaction_TINKER
except:
    print "Tinker module import failed; check SimTK package (required for units)"

try:
    from openmmio import AbInitio_OpenMM, Liquid_OpenMM
except:
    print "OpenMM module import failed; check OpenMM package"

try:
    from abinitio_internal import AbInitio_Internal
except:
    print "Internal energy fitting module import failed"

try:
    from counterpoise import Counterpoise
except:
    print "Counterpoise module import failed"

try:
    from amberio import AbInitio_AMBER
except:
    print "Amber module import failed"

try:
    from psi4io import THCDF_Psi4
except:
    print "PSI4 module import failed"

## The table of implemented Targets
Implemented_Targets = {
    'ABINITIO_GMX':AbInitio_GMX,
    'ABINITIO_TINKER':AbInitio_TINKER,
    'ABINITIO_OPENMM':AbInitio_OpenMM,
    'ABINITIO_AMBER':AbInitio_AMBER,
    'ABINITIO_INTERNAL':AbInitio_Internal,
    'VIBRATION_TINKER':Vibration_TINKER,
    'LIQUID_OPENMM':Liquid_OpenMM,
    'COUNTERPOISE':Counterpoise,
    'THCDF_PSI4':THCDF_Psi4,
    'INTERACTION_TINKER':Interaction_TINKER,
    'BINDINGENERGY_TINKER':BindingEnergy_TINKER,
    'MOMENTS_TINKER':Moments_TINKER,
    'MONOMER_QTPIE':Monomer_QTPIE,
    }
