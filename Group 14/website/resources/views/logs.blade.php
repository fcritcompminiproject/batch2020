@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-8">
            <div class="card">
                <div class="card-header">{{ $employee }}</div>

                <div class="card-body">
                    @if (session('status'))
                        <div class="alert alert-success" role="alert">
                            {{ session('status') }}
                        </div>
                    @endif

                    <table class="table floatLeft">
                        <thead>
                            <tr>
                                <th>Entry Time</th>
                            </tr>
                        </thead>
                        <tbody>
                            @foreach($employee_entry_record as $entry)
                                <tr>
                                    <td>{{ $entry->time }}</td>
                                </tr> 
                            @endforeach
                        </tbody>
                    </table>

                    <table class="table floatRight">
                        <thead>
                            <tr>
                                <th>Exit Time</th>
                            </tr>
                        </thead>
                        <tbody>
                            @foreach($employee_exit_record as $exit)
                                <tr>
                                    <td>{{ $exit->time }}</td>
                                </tr> 
                            @endforeach
                        </tbody>
                    </table>

                </div>
            </div>
        </div>
    </div>
</div>
@endsection
