import h5py

from rball import ResponseDatabase


class PolarResponse(ResponseDatabase):
    @classmethod
    def from_hdf5(cls, file_name: str, use_high_gain: bool = False):

        with h5py.File(file_name, "r") as f:

            # this part is a little polar specific at the moment
            # will remove and generalize

            if use_high_gain:

                ext = "hg"

            else:

                ext = "lg"

            list_of_matrices = f[f"matrix_{ext}"][()]

            theta = f["theta"][()]

            phi = f["phi"][()]

            ebounds = f["ebounds"][()]

            mc_energies = f["mc_energies"][()]

            return cls(
                list_of_matrices=list_of_matrices,
                theta=theta,
                phi=phi,
                ebounds=ebounds,
                monte_carlo_energies=mc_energies,
            )

    def _transform_to_instrument_coordinates(self, ra: float, dec: float):

        return super()._transform_to_instrument_coordinates(ra, dec)
