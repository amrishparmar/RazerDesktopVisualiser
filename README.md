# RazerDesktopVisualiser

An application for visualising your PC desktop on your Razer Chroma keyboard. Created at AnvilHackIV.

*Note*: It currently works best on full size keyboards. Though it will work on Razer laptop or TE keyboards, the right-hand side will be slightly cut-off.

The functionality this program offers is now built-in to the latest builds of Synapse 3, so just use that if you have it. Although this is still useful if you're using Synapse 2.

## Running the program
Minimum requirements:
- Razer SDK core components (this is installed automatically with Razer Synapse) [tested on v2.10]  
- A Razer Chroma-enabled keyboard

The simplest way to run the application is the grab the latest executable from the [releases page](https://github.com/amrishparmar/RazerDesktopVisualiser/releases).

### Running from source
To run from source the following additional requirements are needed:
- Python 3
- Requests
- Pillow

Run the following: `python3 visualiser.py` and enjoy the lightshow.
