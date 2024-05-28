# Use a lightweight base image (e.g., Debian)
FROM gcc:latest

# Install dependencies
RUN apt-get update && \
    apt-get install -y build-essential cmake git

# Create a working directory inside the container
WORKDIR /app

# Copy your source code
COPY . .

# Build your project using CMake
RUN cd build && \
    cmake .. && \
    make

# Expose the port your server listens on (replace with your actual port)
EXPOSE 8080

# Command to run your server when the container starts
CMD ["./build/task"]
