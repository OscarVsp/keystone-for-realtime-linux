# Preparing the board

## Flashing the image

If you are using the provided ready-to-use image, you can find them under TODO.
If you are building the image yourself, the images will be generated under `keystone-rt/(...)/buildroot.build/images/sdcard.img`.


You can flash them into an µSD card using the following command.

```bash
sudo dd if=images/hifive_unmatched64.img of=/path/to/sd/card bs=1M status=progress
```

## Hifive Unmatched 

To boot from the SD card, the physical boot mode DIP switches `MSEL[3:0]` need to be set to `1001`

![alt text](/figures/MSEL.png)


## Connection to the boards

Once the sd card in plugged in and the HiFive Unmatched board is powered up, you can either connect to it using SSH or via the serial connection of the board (using screen or minicon) with baudrate set at `115200`

`sudo screen -L /path/to/dev 115200`

The root password is `hifive`.

See [docs/running-the-experiments.md](docs/running-the-experiments.md) to run the experiment.