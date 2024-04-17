<?php
namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Models\Product;

class ProductAPIController extends Controller{
    public function index(){
        $products = Product::all();
        return response()->json($products);
    }

    public function store(Request $request){
        $request->validate([
            'name' => 'required|max:255',
            'price' => 'required|numeric'
        ]);

        $product = new Product;
        $product->name = $request->name;
        $product->price = $request->price;
        $product->save();

        return response()->json([
            "message" => "Product berhasil di tambahkan"
        ], 201);
    }

    public function edit(Request $request, $id){
        $request->validate([
            'name' => 'required|max:255',
            'price' => 'required|numeric',
        ]);

        $product = Product::findOrFail($id);
        $product->name = $request->name;
        $product->price = $request->price;
        $product->save();

        return response()->json([
            'message' => 'Product updated berhasil',
            'product' => $product
        ]);
    }

    public function destroy($id){
        $product = Product::findOrFail($id);
        $product->delete();

        return response()->json([
            'message' => 'Product deleted berhasil'
        ]);
    }


}