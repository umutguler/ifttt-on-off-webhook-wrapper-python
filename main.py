"""
Python script to control devices via IFTTT.
Example usage is to turn on/off TP-Link Smart Plugs.
"""
import click
from ifttt_on_off import IftttOnOff


@click.command()
@click.option('--on', is_flag=True, help='Turn on the IFTTT integrated device')
@click.option('--off', is_flag=True, help='Turn off the IFTTT integrated device')
def main(on, off):
    """
    Main function to control the speakers via IFTTT.
    """
    if on and off:
        print("Error: You cannot specify both --on and --off.")
        return
    if not on and not off:
        print("Error: You must specify either --on or --off.")
        return

    print("Attempting to", "turn on" if on else "turn off", "via IFTTT")
    ifttt_control = IftttOnOff()
    if on:
        ifttt_control.turn_on()
    else:
        ifttt_control.turn_off()


if __name__ == "__main__":
    # pylint: disable = no-value-for-parameter
    main()
