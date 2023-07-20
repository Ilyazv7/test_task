terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  token     = "y0_AgAAAABvWhydAATuwQAAAADn0Yyjc6uPyV8uTW-O9TW7NhtPB_euJjY"
  cloud_id  = "b1g213361b84e65uptss"
  folder_id = "b1gi1cqqu127k2ga98cv"
  zone      = "ru-central1-a"
}

resource "yandex_vpc_network" "taskvpc" {
  name = "ilyadev"
}

resource "yandex_vpc_subnet" "devtask" {
  v4_cidr_blocks = ["10.2.0.0/16"]
  network_id     = yandex_vpc_network.taskvpc.id
}

data "yandex_compute_image" "ubuntu_image" {
  family = "ubuntu-2004-lts"
}

resource "yandex_compute_instance" "devtaskserver" {
  name        = "devtaskserver"
  platform_id = "standard-v1"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.ubuntu_image.id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.devtask.id
    nat       = true
  }

  metadata = {
    ssh-keys  = "${file("~/.ssh/id_rsa.pub")}"
    user-data = "${file("./meta.yml")}"
  }
}
