package com.maboglia.film.repos;

import org.springframework.data.jpa.repository.JpaRepository;

import com.maboglia.film.entities.Film;

public interface FilmRepo extends JpaRepository<Film, Integer> {

}
