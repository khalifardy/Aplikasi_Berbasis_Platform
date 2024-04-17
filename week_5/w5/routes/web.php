<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Lat1Controller;
use App\Http\Controllers\ProductController;
use App\Http\Controllers\ProductAPIController;


Route::get('/', function () {
    return view('welcome');
});

Route::get('/latihan1',[Lat1Controller::class, 'index']);
Route::get('/latihan1/m2',[Lat1Controller::class, 'method2']);
Route::get('/product',[ProductController::class, 'index']);
Route::get('/product/create',[ProductController::class, 'create']);
Route::get('/product/{id}/edit',[ProductController::class, 'edit']);
Route::post('/product/api/tambah',[ProductController::class, 'store']);
Route::put('/product/api/{id}',[ProductController::class, 'update']);
Route::delete('/product/hapus/{id}',[ProductController::class, 'destroy']);
Route::put('/product/api2/{id}',[ProductAPIController::class, 'edit']);
Route::get('/product/api',[ProductAPIController::class, 'index']);
Route::post('/product/api',[ProductAPIController::class, 'store']);
Route::delete('/product/api2/delete/{id}',[ProductAPIController::class, 'destroy']);
