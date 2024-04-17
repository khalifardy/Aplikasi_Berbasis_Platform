<?php
namespace App\Http\Controllers;

class Lat1Controller extends Controller
{
    public function index(){
        $data["nama"]="Khalifardy Miqdarsah";
        $data["asal"]="Bekasi";
        return view('v_latihan1', $data);
    }

    public function method2(){
		$data['title'] = "Daftar Mahasiswa";
		$data['daf_mhs'] = array(
			array("nama" => "Miko", "asal" => "Bekasi"),
	 	   array("nama" => "Ayu", "asal" => "Blitar"),
			array("nama" => "Ali", "asal" => "Surabaya")
		);
		return view('v_latihan2', $data);
	}


}