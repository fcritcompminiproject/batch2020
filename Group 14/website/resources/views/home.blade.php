@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">Employees</div>

                <div class="card-body">
                    @if (session('status'))
                        <div class="alert alert-success" role="alert">
                            {{ session('status') }}
                        </div>
                    @endif

                    <div class="links">

                        @foreach($employees as $employee)

                        <a href="/logs/{{{$employee->name}}}">{{{$employee->name}}}</a>
                        
                        @endforeach
                        <!-- <a href="/logs/siddhesh">Siddhesh</a>
                        <a href="/logs/sandesh">Sandesh</a>
                        <a href="/logs/yash">Yash</a> -->

                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
