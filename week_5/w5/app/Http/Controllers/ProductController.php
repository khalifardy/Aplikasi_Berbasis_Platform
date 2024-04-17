<?php
namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Models\Product;

class ProductController extends Controller
{
    public function index(){
        $prods = Product::get();
        return view('product.product_list', ['list' => $prods]);
    }
    
    public function create(){
	    return view('product.form_tambah', [
	      'title' => 'Tambah',
	      'method' => 'POST',
	      'action' => 'product/api/tambah'
     ]);
   }

    public function store(Request $request){
	    $prod = new Product;
	    $prod->name = $request->name;
	    $prod->price = $request->price;
	    $prod->save();
	    return redirect('/product')->with('msg', 'Tambah berhasil');
    }

    public function show($id){
	    return Product::find($id);
    }

    public function edit($id){
	    return view('product.form_edit', [
	      'title' => 'Edit',
	      'method' => 'PUT',
	      'action' => "product/api/$id",
	      'data' => Product::find($id)
        ]);
    }

    public function update(Request $request, $id){
	    $prod = Product::find($id);
	    $prod->name = $request->name;
	    $prod->price = $request->price;
	    $prod->save();
	    return redirect('/product')->with('msg', 'Edit berhasil');
    }

    public function destroy($id){
        Product::destroy($id);
      // atau
      /* $prod = Product::find($id);
	    $prod->delete(); */
	    return redirect('/product')->with('msg', 'Hapus berhasil');
    }
}