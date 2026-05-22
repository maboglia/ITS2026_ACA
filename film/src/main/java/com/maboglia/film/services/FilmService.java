package com.maboglia.film.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.maboglia.film.entities.Film;
import com.maboglia.film.repos.FilmRepo;

@Service
public class FilmService {


    @Autowired
    private FilmRepo repo;

    public List<Film> getAll() {
        return repo.findAll();
    }

    public Film addFilm(Film f) {
        return repo.save(f);
    }


}
