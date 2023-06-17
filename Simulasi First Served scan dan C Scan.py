# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 07:31:48 2023

@author: Fernanda
"""

def fcfs(jobs, head):
    total_movement = 0
    current_track = head

    for job in jobs:
        total_movement += abs(job - current_track)
        current_track = job

    return total_movement


def scan(jobs, head, direction, disk_size):
    total_movement = 0
    current_track = head

    if direction == "left":
        sorted_jobs = [job for job in jobs if job < head]
        sorted_jobs.sort(reverse=True)
        sorted_jobs += [job for job in jobs if job >= head]
    else:
        sorted_jobs = [job for job in jobs if job >= head]
        sorted_jobs.sort()
        sorted_jobs += [job for job in jobs if job < head]

    for job in sorted_jobs:
        total_movement += abs(job - current_track)
        current_track = job

    return total_movement


def c_scan(jobs, head, direction, disk_size):
    total_movement = 0
    current_track = head

    if direction == "left":
        sorted_jobs = [job for job in jobs if job < head]
        sorted_jobs.sort(reverse=True)
        sorted_jobs += [disk_size - 1] + [job for job in jobs if job >= head] + [0]
    else:
        sorted_jobs = [job for job in jobs if job >= head]
        sorted_jobs.sort()
        sorted_jobs += [0] + [job for job in jobs if job < head] + [disk_size - 1]

    for job in sorted_jobs:
        total_movement += abs(job - current_track)
        current_track = job

    return total_movement


# Input dari pengguna
jobs = input("Masukkan daftar pekerjaan (pisahkan dengan spasi): ").split()
jobs = [int(job) for job in jobs]

head = int(input("Masukkan posisi kepala: "))
direction = input("Masukkan arah pergerakan (left/right): ")
disk_size = int(input("Masukkan ukuran disk: "))

# Menampilkan hasil
print("Total pergerakan FCFS:", fcfs(jobs, head))
print("Total pergerakan SCAN:", scan(jobs, head, direction, disk_size))
print("Total pergerakan C-SCAN:", c_scan(jobs, head, direction, disk_size))
