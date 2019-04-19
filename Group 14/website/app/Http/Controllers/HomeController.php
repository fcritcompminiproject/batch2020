<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;

class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function index()
    {
        $employees= DB::table('employees')->get();
        return view('home')->with('employees', $employees);
    }

    public function logs($employee)
    {
        $employee_entry_record = DB::table('mini')->where('name',$employee)->where('type','In')->get();
        $employee_exit_record = DB::table('mini')->where('name',$employee)->where('type','Out')->get();

        return view('logs2')->with('employee_entry_record',$employee_entry_record)->with('employee_exit_record',$employee_exit_record)->with('employee',$employee);

        /*return $employee_entry_record;*/
        /*return $employee_exit_record;*/
    }
}
