package com.maboglia.film.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.maboglia.film.entities.Film;
import com.maboglia.film.services.FilmService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;



@RestController
@RequestMapping("/api/films")
public class FilmRest {

    @Autowired
    private FilmService service;

    @GetMapping("")
    public List<Film> getAll() {
        return service.getAll();
    }

    @PostMapping("")
    public Film addFilm(@RequestBody Film f) {
        return service.addFilm(f);
    }
    
    @PostMapping("/tanti")
    public String addTantiFilm(@RequestBody List<Film> lista) {

        for(Film f: lista) {
            service.addFilm(f);
        }

        return "Films added successfully";
    }
    
    

}
