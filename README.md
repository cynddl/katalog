# Katalog

Katalog is a WIP project aiming to keep trace of a multimedia database over multiple supports.


## Motivation

Storing a large number of music or movie files will likely become a painful issue.
Especially if you want to save your files in multiple hard disks, or somewhere
online.

The goal of katalog is to keep trace of all these files, even when they are
renamed or moved, and to assist the search process.


## Roadmap

- [ ] Write import and sync of files (probably using a bipartite graph for new files).
- [ ] Analyze :clapper: & :sound: to integrate metadata.
- [ ] Add a minimal CLI to manipulate the data.


### CLI Example

    katalog add /Volumes/MyMovies

    katalog sync -vv
    Syncing /Volumes/MyMovies
    > 22 new files
    > 3 renamed files
    > 10 deleted files (missing in the disk)
