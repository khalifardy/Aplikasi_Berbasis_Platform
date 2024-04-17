<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ProductAPIController;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');
Route::get('/product/api',[ProductAPIController::class, 'index']);
Route::post('/product/api',[ProductAPIController::class, 'store']);