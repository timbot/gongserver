
# Gong Server

A simple webserver that plays a sound on any HTTP request.

## Installation

This server requires Python 3 and `mpg123`.

On a Debian-based system (like Raspberry Pi OS), you can install `mpg123` with:

```bash
sudo apt-get update
sudo apt-get install mpg123
```

## Usage

1.  **Start the server:**

    ```bash
    python3 gongserver.py --sound-file /path/to/your/sound.mp3
    ```

    You can also specify a port (default is 8000):

    ```bash
    python3 gongserver.py --sound-file /path/to/your/sound.mp3 --port 8080
    ```

2.  **Trigger the sound:**

    Make an HTTP request to the server. You can do this from another terminal using `curl`:

    ```bash
    curl http://localhost:8000
    ```

    Or simply by visiting `http://<raspberry-pi-ip>:8000` in a web browser.

    Each time a request is made, the sound will play.

## Running as a Service (on Raspberry Pi)

To have the gong server start automatically on boot, you can set it up as a `systemd` service.

1.  **Copy the example service file:**

    ```bash
    sudo cp gong.service.example /etc/systemd/system/gong.service
    ```

2.  **Edit the service file:**

    Open the new service file with a text editor:

    ```bash
    sudo nano /etc/systemd/system/gong.service
    ```

    You **must** change the following paths to be the correct **absolute paths** for your system:
    *   `ExecStart`: Update the path to `gongserver.py` and the path to your sound file.
    *   `WorkingDirectory`: Update this to the directory where `gongserver.py` is located.
    *   `User`: Change this if you are not running as the default `pi` user.

3.  **Enable and start the service:**

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable gong.service
    sudo systemctl start gong.service
    ```

4.  **Check the status:**

    You can check if the service is running correctly with:

    ```bash
    sudo systemctl status gong.service
    ```
