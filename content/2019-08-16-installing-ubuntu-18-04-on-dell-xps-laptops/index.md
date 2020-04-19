---
date: 2019-08-16
title: Installing Ubuntu 18.04 on Dell XPS Laptops
cover: ./images/Screenshot-from-2018-12-22-14-30-48.webp
categories:
    - Tech
tags:

    - Ubuntu

---

About a month ago, I started a new job in St. Louis, Missouri. Upon arrival, I was given a Dell XPS 500 laptop for my dev machine. Immediately, I formatted the drive and installed Ubuntu 18.04. Well, I tried at least. 

When installing Ubuntu 18.04 (or any recent-ish version) on a Dell XPS laptop, there are a few special things you have to do first. This is due to the Nvidia graphics cards not playing well with Ubuntu. After much trial and error, I finally figured out how to get Ubuntu to play well with Dell XPS laptops.

Follow these steps:

1. Disable Fast Boot and Secure Boot (or Secure loader) in the Bios.

2. Plug in the bootable USB with the Linux distro (mine was Ubuntu 18.04)

3. When you see the loader to "Install Ubuntu" etc ... press "e" and edit a line:
Replace `quiet splash` to `nomodeset` and press F10 to boot.

Then after the installation is complete, you will have to reboot.

4. This time you will need to load the GRUB menu, (Hold Shift after bios splash and before the OS logo shows up, if You see the logo, you're too late. Again, press "e" and edit a line:
In the line that starts with `linux`, add `nouveau.modeset=0` at the end of that line. (keep `nomodeset` from before)

5. After booting linux install the nvidia drivers.

Run `ubuntu-drivers devices`. We can see the current video card and the recommend driver. If you agree with that recommendation, run `sudo ubuntu-drivers autointsall`.
If you do not agree with the recommendation, you can install the individual driver by `sudo apt-get install nvidia-384`.

Reboot. And then it's done.