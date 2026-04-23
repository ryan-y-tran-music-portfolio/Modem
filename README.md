# Modem

## What did I do?

I made a demodulator for a simplified version of the Bell 103 modem protocol. My program takes a secret message that was generated as a WAV file [here](https://www.po8.org/modem-messages/ryatran.wav) (you can generate different secret messages if you change the name of the WAV in the link), and converts each bit into another bit based on whever it is a mark frequency (2225 Hz sine wave) or space frequency (2025 Hz sine wave); the data bits are then extracted, packed into bytes, and those bytes are converted into ASCII. The decoded ASCII is available in the same directory as this program.

## How did it Go?

Building the program went generally well. When I was building the tone detector, I was wondering why the ratio for tone power wasn't what I was expected, but it turned out that it depended on N; a larger N produces a larger ratio, and vise versa. I also had to figure out the best way to store bytes and how to actually gather the right bits for those bytes.

## What's next?

The program currently depends on the user manually generating a WAV file and inserting it into the same directory, however it would be neat if the program can automatically do it, getting a secret message based on user input. Other stuff can be added to make this more fun: properly synchronize to find the starting byte of the message rather than assuming the alignment is fixed from sample 0.

## How to Build

### Installing uv

Follow the instructions to install the uv package manager [here](https://docs.astral.sh/uv/getting-started/installation/).

### Running the Program

Generate your secret message and save the WAV file in the same directory as this program as message.wav. Then, simply run this program via `uv run modem.py`
